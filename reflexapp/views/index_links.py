import reflex as rx
from reflexapp.components.link_button import link_button
from reflexapp.components.title import title
import reflexapp.views.constants as constants
import reflexapp.routes.routes as routes


def index_links() -> rx.Component:
    return rx.vstack(
        title("Resume"),
        link_button(
            "Look at my resume",
            "Programming and English studies",
            "/resume.svg",
            routes.Route.RESUME.value,
            is_external=False
        ),
        title("Projects"),
        link_button(
            "GitHub Repositories",
            "Angular, HTML, CSS, JS, NodeJs(ExpressJs), SQL, Supabase, Reflex and Python.",
            "/github.svg",
            routes.Route.PROJECTS.value,
            is_external=False
        ),

        title("My Social Networks"),
        link_button(
            "LinkedIn",
            "My Linkedin profile with more information.",
            "/linkedin.svg",
            constants.LINKEDIN_URL
        ),
        link_button(
            "GitHub",
            "My GitHub profile with all my projects and stats.",
            "/github.svg",
            constants.GITHUB_URL
        ),
        title("Contact"),
        link_button(
            "Contact me",
            "Send me an email.",
            "/contacto.svg",
            constants.CONTACT
        ),
        width="100%",
        align_items="start"
    )
