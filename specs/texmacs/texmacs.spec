# $Id: $

# Authority: dries
# Screenshot: http://www.texmacs.org/Samples/texmacs-1.png
# ScreenshotURL: http://www.texmacs.org/tmweb/home/screenshots.en.html

Summary: Structured WYSIWYG scientific text editor
Name: texmacs
Version: 1.0.4.2
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.texmacs.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp.texmacs.org/pub/TeXmacs/targz/TeXmacs-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tetex-latex, guile-devel

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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot} \
	includedir=%{_includedir} \
	bindir=%{_bindir} \
	mandir=%{_mandir}
%{__install} -D %{buildroot}%{_datadir}/TeXmacs/misc/mime/texmacs.desktop %{buildroot}%{_datadir}/applications/texmacs.desktop

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
* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.4.2-1
- Initial package.

