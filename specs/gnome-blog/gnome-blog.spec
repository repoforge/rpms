# $Id$
# Authority: hadams

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define desktop_vendor rpmforge

Summary: GNOME panel object for posting blog entries
Name: gnome-blog
Version: 0.9.1
Release: 5%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.gnome.org/~seth/gnome-blog/

Source: http://ftp.gnome.org/pub/gnome/sources/gnome-blog/0.9/gnome-blog-%{version}.tar.bz2
Patch0: gnome-blog-bonobo.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: GConf2
BuildRequires: glib2-devel
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: perl(XML::Parser)
BuildRequires: pygtk2-devel >= 2.6
Requires: GConf2
Requires: gnome-python2-applet
Requires: gnome-python2-gconf
Requires: gnome-python2-gnomevfs
Requires: gnome-python2-gtkspell
Requires: pygtk2

%description
GNOME panel object that allows convenient posting of blog entries to
any blog that supports the bloggerAPI.

%prep
%setup
%patch0 -p1 -b .bonobo

%build
%configure --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

desktop-file-install --delete-original                   \
    --vendor="%{desktop_vendor}"                         \
    --add-category="Network" --remove-category="Utility" \
    --dir="%{buildroot}%{_datadir}/applications"         \
    %{buildroot}%{_datadir}/applications/gnome-blog.desktop

%pre
if [ $1 -gt 1 ]; then
    export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
    gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/gnomeblog.schemas >/dev/null || :
fi


%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/gnomeblog.schemas >/dev/null || :


%preun
if [ $1 -eq 0 ]; then
    export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
    gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/gnomeblog.schemas >/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%config %{_sysconfdir}/gconf/schemas/gnomeblog.schemas
%{_bindir}/gnome-blog-poster
%{_datadir}/applications/%{desktop_vendor}-gnome-blog.desktop
%{_datadir}/gnome-2.0/ui/GNOME_BlogApplet.xml
%{_datadir}/pixmaps/gnome-blog.png
%{_libdir}/bonobo/servers/GNOME_BlogApplet.server
%{_libexecdir}/blog_applet.py
%{_libexecdir}/blog_applet.pyc
%ghost %{_libexecdir}/blog_applet.pyo
%{python_sitelib}/gnomeblog/
%ghost %{python_sitelib}/gnomeblog/*.pyo
%exclude %{python_sitelib}/gnomeblog/gnome-blog-poster

%changelog
* Wed Oct 31 2007 Heiko Adams <info [at] fedora-blog [dot] de> - 0.9.1-5
- Rebuild for RPMforge.

* Wed Sep  6 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.9.1-4
- Don't ghost *.pyo files.

* Sun Sep  3 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.9.1-3
- Rebuild for FC6.
- Use --disable-schemas-install with config.
- Add BR perl(XML::Parser).

* Wed Jun 21 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.9.1-2
- Update to 0.9.1.
- Add patch to fix bonobo.
- Bump version of pygtk2.
- Cleanup scriptlets.
- Drop poster patch & makefile patchs.

* Sun Mar 26 2006 Brian Pepple <bdpepple@ameritech.net> - 0.8-13
- Rebuild.

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 0.8-12
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Feb  7 2006 Brian Pepple <bdpepple@ameritech.net> - 0.8-11
- Remove Utility category from desktop file. (#179827)

* Sun Jan 15 2006 Brian Pepple <bdpepple@ameritech.net> - 0.8-10
- Bump for FC5 rebuild.
- Added some macros.

* Sun May 22 2005 Brian Pepple <bdpepple@ameritech.net> - 0.8-9
- Bump release > than FC3 version.
- Add requires for gnome-python2-gtkspell.

* Mon May  9 2005 Brian Pepple <bdpepple@ameritech.net> - 0.8-7
- Remove hard-coded dist tag.
- Removed unused sitearch definition.

* Wed Mar 30 2005 Brian Pepple <bdpepple@ameritech.net> - 0.8-6.fc4
- Rebuild with Python 2.4.
- Add dist tag.

* Tue Mar  1 2005 Brian Pepple <bdpepple@ameritech.net> - 0.8-5
- Add build requires: intltool
- Drop epoch: 0.

* Mon Feb  7 2005 Brian Pepple <bdpepple@gmail.com> - 0:0.8-4
- Added patch to correct blog-poster bug.(#2377c5)

* Thu Feb 03 2005 Toshio Kuratomi <toshio@tiki-lounge.com> - 0:0.8-0.fdr.3
- No longer include gnome-blog-poster in the library path.  It only belongs
  in the bindir.
- Switch to the new python macros for python-abi.
- Switch to python_sitelib in the files section.  Makes gnome-blog build on
  x86_64.
- Change group to Applications/Internet.

* Thu Jan 13 2005 Brian Pepple <bdpepple@gmail.com> - 0:0.8-0.fdr.2
- Added makefile patch to fix python byte compiling from Toshio Kuratomi (#2377).

* Wed Jan 12 2005 Brian Pepple <bdpepple@gmail.com> - 0:0.8-0.fdr.1
- Updated to 0.8.
- Removed code from spec file that fixed location of blog_applet.py, since this was corrected upstream.
- Added requires for gnome-python2-gnomevfs.

* Tue Feb  3 2004 Brian Pepple <bdpepple@ameritech.net> 0:0.7-0.fdr.7
- Removed Requires: GConf2, and replaced with Requires(post,preun).

* Tue Feb  3 2004 Brian Pepple <bdpepple@ameritech.net> 0:0.7-0.fdr.6
- Added GConf requirement, and removed PreReq on gconftool-2.
- Under %file, changed static python location with appropriate variables.
- Added gnome-blog subdir to %files.
- Changed source permissions to 644.
- Added fix for libexec of blog-applet.py

* Mon Feb 02 2004 Toshio Kuratomi <toshio@tiki-lounge.com> 0:0.7-0.fdr.5
- Add Epoch to Requires that have versions
- Cleanup postin/preun scripts for schema install/uninstall
- And get rid of call to ldconfig
- Make package noarch
- Require python version because of python2.2/site-lib directory
- Remove GConf2 as a prereq because gconftool-2 will pull it in.
- Remove INSTALL file from docs (generic INSTALL)
- Change Source0 to point to ftp.gnome.org
- Use desktop-file-install to install the desktop file with --vendor=fedora,
  and adding the X-Fedora and Network categories
- We don't need both .pyc and .pyo files so %ghost the pyo's

* Thu Jan  8 2004 Brian Pepple <bdpepple@ameritech.net> 0:0.7-0.fdr.4
- added gettext build requirement.

* Thu Jan  1 2004 Brian Pepple <bdpepple@ameritech.net> 0:0.7-0.fdr.3
- More clean up of spec file.

* Wed Dec 31 2003 Brian Pepple <bdpepple@ameritech.net> 0:0.7-0.fdr.2
- Clean up of spec file.

* Mon Dec 22 2003 Brian Pepple <bdpepple@ameritech.net> 0:0.7-0.fdr.1
- Initial Fedora build.
