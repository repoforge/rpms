# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Image browser and viewer
Name: gqview
Version: 2.0.4
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://gqview.sourceforge.net/

Source: http://dl.sf.net/sourceforge/gqview/gqview-%{version}.tar.gz
Patch1: gqview-2.0.0-editors.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, gtk2-devel >= 2.4
Requires: desktop-file-utils

%description
GQview is an image viewer for browsing through graphics files. GQview
features include single click file viewing, support for external
editors, previewing images using thumbnails, and zoom.

%prep
%setup
%patch1 -p1 -b .editors

%{__perl} -pi.orig -e '
		s|^#define\s+GQVIEW_HELPDIR.*$|#define GQVIEW_HELPDIR "%{_docdir}/gqview-%{version}"|;
		s|^#define\s+GQVIEW_HTMLDIR.*$|#define GQVIEW_HTMLDIR "%{_docdir}/gqview-%{version}/html"|;
	' configure
	
%{__perl} -pi.orig -e '
		s|^Name=GQview$|Name=GQview Image Viewer|;
		s|^Comment=Image Viewer$|Comment=View and organize images|;
	' gqview.desktop

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Clean up buildroot
%{__mv} -vf %{buildroot}%{_docdir}/gqview-%{version}/ rpm-doc/

%post
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun
update-desktop-database %{_datadir}/applications &> /dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO rpm-doc/html/
%doc %{_mandir}/man1/gqview.1*
%{_bindir}/gqview
%{_datadir}/applications/gqview.desktop
%{_datadir}/pixmaps/gqview.png

%changelog
* Sun Apr 03 2007 Dag Wieers <dag@wieers.com> - 2.0.4-1
- Initial package. (using DAR)
