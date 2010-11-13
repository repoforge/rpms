# $Id$
# Authority: dries

Summary: LaTeX Editor
Name: amyedit
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://sourceforge.net/projects/amyedit/

Source: http://dl.sf.net/amyedit/amyedit-%{version}.tar.bz2
Patch0: makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtkmm24-devel, gcc-c++, pkgconfig, glibmm-devel
BuildRequires: glib2-devel, libsigc++2-devel, pango-devel, gtk2-devel
BuildRequires: desktop-file-utils

%description
AmyEdit is a gtkmm LaTeX Editor designed to allow easier creation of LaTeX
documents for users new to linux. See TODO for information on lacking
features and Changelog for an up to date list of new features.

AmyEdit currently features tabbed-editing, word count, new document templates
preview your document using pdflatex and xpdf (configurable in preferences)
as well as an export feature. Output from these commands is displayed in a
paned view.

%prep
%setup
%patch0 -p1

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=AmyEdit
Comment=LaTeX editor
Exec=amyedit
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Office;X-Red-Hat-Extra;
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{_datadir}/doc

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING INSTALL README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop

%changelog
* Thu Mar 16 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Sun Mar 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Tue Feb 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Updated to release 0.7.

* Wed Dec 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Initial package.

