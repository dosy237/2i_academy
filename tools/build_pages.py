# Génère toutes les pages du site : python3 tools/build_pages.py
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pages_main, pages_programs, pages_forms, pages_legal  # noqa: E402

BUILDERS = [
    pages_main.build_index, pages_main.build_ecole, pages_main.build_pedagogie, pages_main.build_entreprises,
    pages_main.build_formations, pages_main.build_brochures,
    pages_programs.build_bachelor, pages_programs.build_mastere, pages_programs.build_emba, pages_programs.build_ia,
    pages_forms.build_admissions, pages_forms.build_candidature, pages_forms.build_contact, pages_forms.build_merci,
    pages_legal.build_mentions, pages_legal.build_confidentialite, pages_legal.build_accessibilite,
    pages_legal.build_plan, pages_legal.build_404,
]

if __name__ == "__main__":
    for build in BUILDERS:
        build()
    print(f"{len(BUILDERS)} pages générées.")
