import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Bot token - environment variable
Token = os.getenv("BOT_TOKEN")

if not Token:
    raise ValueError("BOT_TOKEN environment variable is missing!")

# Initialize the bot application
app = ApplicationBuilder().token(Token).build()

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to Course Master. Use /help command to see all the courses available!")

# Help command
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        /start -> Welcome to the Page
/help -> It shows available Commands 
/courses -> It shows available Courses
/roadmap -> Mastering Programming Language
/problems -> Practice problems to Solve
/projects -> It gives real-time projects
        """
    )

# Course command
async def courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        /C -> Gives C course link
/CPP -> Gives C++ course link
/Python -> Gives Python course link
/Java -> Gives Java course link
/Rust -> Gives Rust course link
        """
    )


# Roadmap - Drive link
async def roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Drive Link: https://drive.google.com/drive/folders/1jp6XBJVH_fbItFL3i2Nvhj1xehJNt31_?usp=sharing")


# Problems Command
async def problems(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey this is a problem. solve it")

# Projects command
async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey this is a project demo")


# Course links
async def C(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for C: https://www.udemy.com/course/c-programming-for-beginners-/")

async def CPP(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for C++: https://www.udemy.com/course/beginning-c-plus-plus-programming/")

async def Python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for Python: https://www.udemy.com/course/learn-python-with-abdul-bari/")

async def Java(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for Java: https://www.udemy.com/course/java-programming-tutorial-for-beginners/")

async def Rust(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link for Rust: https://www.udemy.com/course/rust-lang/")


# Unknown command handler
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sorry, I didn't understand that command. Please use /help to see the list of available commands.")


# Add handlers
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(CommandHandler('roadmap', roadmap))
app.add_handler(CommandHandler('courses', courses))
app.add_handler(CommandHandler('problems', problems))
app.add_handler(CommandHandler('projects', projects))

app.add_handler(CommandHandler('C', C))
app.add_handler(CommandHandler('CPP', CPP))
app.add_handler(CommandHandler('Python', Python))
app.add_handler(CommandHandler('Java', Java))
app.add_handler(CommandHandler('Rust', Rust))

app.add_handler(MessageHandler(filters.COMMAND, unknown))

# Run the bot
if __name__ == "__main__":
    app.run_polling()

# updated help and added courses, roadmap(drive), problems, projects - 08/03/2025
