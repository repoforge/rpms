# $Id: $

# Authority: dries
# Screenshot: http://www.texmacs.org/Samples/texmacs-1.png
# ScreenshotURL: http://www.texmacs.org/tmweb/home/screenshots.en.html

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Structured WYSIWYG scientific text editor
Name: texmacs
Version: 1.0.6.1
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.texmacs.org/

Source: ftp://ftp.texmacs.org/pub/TeXmacs/targz/TeXmacs-%{version}-src.tar.gz
Patch: texmacs-gcc-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tetex-latex, guile-devel, gcc-c++, python
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-proto-devel, libXext-devel}

### Fedora Extras introduced them differently :(
Obsoletes: TeXmacs < %{version}-%{release}

%description
GNU TeXmacs is a free scientific text editor, which was both inspired by TeX
and GNU Emacs. The editor allows you to write structured documents via a
wysiwyg (what-you-see-is-what-you-get) and user friendly interface. New
styles may be created by the user. The program implements high-quality
typesetting algorithms and TeX fonts, which help you to produce
professionally looking documents.


The high typesetting quality still goes through for automatically generated
formulas, which makes TeXmacs suitable as an interface for computer algebra
systems. TeXmacs also supports the Guile/Scheme extension language, so that
you may customize the interface and write your own extensions to the editor.

Converters exist for TeX/LaTeX and they are under development for
Html/MathML/Xml. In the future, TeXmacs is planned to evolve towards a
complete scientific office suite, with spreadsheet capacities, a technical
drawing editor and a presentation mode.

%prep
%setup -n TeXmacs-%{version}-src
%patch -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot} \
	includedir=%{_includedir} \
	bindir=%{_bindir} \
	mandir=%{_mandir}
%{__install} -Dp %{buildroot}%{_datadir}/TeXmacs/misc/mime/texmacs.desktop %{buildroot}%{_datadir}/applications/texmacs.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING LICENSE
%doc %{_mandir}/man?/*
%{_datadir}/TeXmacs
%{_libexecdir}/TeXmacs
%{_bindir}/*
%{_includedir}/*.h
%{_datadir}/applications/*.desktop

%changelog
* Sat May 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.6.1-1
- Update to release 1.0.6.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.6-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.6-1
- Update to release 1.0.6.

* Mon Nov 07 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.12-1
- Update to release 1.0.5.12.

* Wed Oct 19 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.11-1
- Update to release 1.0.5.11.

* Mon Oct 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.10-1
- Update to release 1.0.5.10.

* Wed Sep 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.9-1
- Update to release 1.0.5.9.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.8-1
- Update to release 1.0.5.8.

* Mon Aug 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.7-1
- Update to release 1.0.5.7.

* Mon Jul 25 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.6-1
- Update to release 1.0.5.6.

* Mon Jul 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.5-1
- Update to release 1.0.5.5.

* Tue Jun 21 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.4-1
- Update to release 1.0.5.4.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5.3-1
- Update to release 1.0.5.3.

* Mon Feb 21 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.4.5-1
- Update to release 1.0.4.6.

* Sun Dec 12 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.4.5-1
- Update to release 1.0.4.5.

* Sat Dec 04 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.4.4-1
- Update to release 1.0.4.4.

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.4.3-1
- Update to version 1.0.4.3.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.4.2-1
- Initial package.
