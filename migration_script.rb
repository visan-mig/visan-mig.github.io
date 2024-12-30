require 'yaml'
require 'fileutils'
require 'date'
require 'slugify'

# Create _news_items directory if it doesn't exist
FileUtils.mkdir_p('_news_items')

# Get file creation date from git history or fall back to file stats
def get_file_creation_date(file_path)
  begin
    # Try to get date from git history
    git_date = `git log --follow --format=%aI --reverse "#{file_path}" | head -1`.strip
    unless git_date.empty?
      date = Date.parse(git_date)
      puts "Found git commit date: #{date.strftime('%d %B %Y')}"
      return date
    end
  rescue
    # If git command fails, continue to file stats
  end

  begin
    # Fall back to file stats
    date = File.stat(file_path).birthtime.to_date
    puts "Found file creation date: #{date.strftime('%d %B %Y')}"
    return date
  rescue
    # If all else fails, use today's date
    date = Date.today
    puts "Using today's date: #{date.strftime('%d %B %Y')}"
    return date
  end
end

def parse_date(date_str, file_path)
  return get_file_creation_date(file_path) if date_str.nil? || date_str.empty?
  
  begin
    # Parse date string in format "3 January 2023"
    date = Date.parse(date_str)
    puts "Using provided date: #{date.strftime('%d %B %Y')}"
    return date
  rescue Date::Error
    puts "\nWarning: Could not parse date '#{date_str}', falling back to file date"
    return get_file_creation_date(file_path)
  end
end

def extract_title_and_source(headline)
  return ['No Title', '', ''] if headline.nil? || headline.empty?
  
  # Split by colon and handle cases with and without parentheses
  if headline =~ /(.*?)\((.*?)\):(.*)/
    title = $1.strip
    source = $2.strip
    quoted_title = $3.strip.gsub('"', '').strip
  else
    parts = headline.split(':').map(&:strip)
    title = parts[0]
    quoted_title = parts[1]&.gsub('"', '')&.strip || ''
    source = ''
  end
  [title, source, quoted_title]
end

def create_filename(date, title)
  # Create Jekyll-compatible filename
  date_str = date ? date.strftime('%Y-%m-%d') : Time.now.strftime('%Y-%m-%d')
  slug = (title || 'untitled').slugify
  "#{date_str}-#{slug}.md"
end

def extract_pdf_link(content)
  return nil if content.nil? || content.empty?
  # Extract PDF link from markdown content
  if content =~ /\[.*?\]\((.*?\.pdf)\)/
    $1
  else
    nil
  end
end

# Read the news.yml file
yaml_path = '_data/news.yml'
news_data = YAML.load_file(yaml_path)

# Process each news item
news_data.each_with_index do |item, index|
  begin
    puts "\nProcessing item #{index + 1}..."
    
    # Skip if item is nil or not a hash
    unless item.is_a?(Hash)
      puts "Warning: Skipping invalid item #{index + 1}"
      next
    end

    date = parse_date(item['date'], yaml_path)
    if date.nil?
      puts "Warning: Could not determine date for item #{index + 1}"
      next
    end

    title, source, quoted_headline = extract_title_and_source(item['headline'])
    pdf_link = extract_pdf_link(item['content'])
    
    # Create front matter
    front_matter = {
      'layout' => 'news_item',
      'title' => title,
      'date' => date.strftime('%Y-%m-%d'),
      'source' => source,
      'headline' => quoted_headline,
      'pdf_link' => pdf_link
    }

    # Create content for the markdown file
    content = ["---"]
    content << front_matter.to_yaml.strip
    content << "---"
    content << ""
    content << (item['content'] || '').strip

    # Generate filename
    filename = create_filename(date, title)
    filepath = File.join('_news_items', filename)

    # Write the file
    File.write(filepath, content.join("\n"))
    puts "Created: #{filepath}"
  rescue => e
    puts "Error processing item #{index + 1}: #{e.message}"
    puts "Item content: #{item.inspect}"
    puts "Continuing with next item..."
  end
end

puts "\nMigration complete!"
puts "Remember to:"
puts "1. Install required gems (jekyll-paginate-v2)"
puts "2. Update _config.yml with collections and pagination settings"
puts "3. Create the news_item layout"
puts "4. Update the main news.html page"