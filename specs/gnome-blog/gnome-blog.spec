# $Id$
# Authority:    hadams

%define gnome_python2_version 2.6
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		gnome-blog
Version:	0.9.1
Release:	5
Summary:	GNOME panel object for posting blog entries

Group:		Applications/Internet
License:	GPL
URL:		http://www.gnome.org/~seth/gnome-blog/		
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch1:		%{name}-bonobo.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	gnome-python2-applet >= %{gnome_python2_version}
Requires:	gnome-python2-gconf  >= %{gnome_python2_version}
Requires:	gnome-python2-gnomevfs >= %{gnome_python2_version}
Requires:	gnome-python2-gtkspell
Requires:	pygtk2 >= %{gnome_python2_version}

Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

BuildRequires:	pygtk2-devel >= %{gnome_python2_version}
BuildRequires:	glib2-devel
BuildRequires:	gettext
BuildRequires:	GConf2
BuildRequires:	desktop-file-utils
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool


%description
GNOME panel object that allows convenient posting of blog entries to
any blog that supports the bloggerAPI.


%prep
%setup -q
%patch1 -p1 -b .bonobo


%build
%configure --disable-schemas-install
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

desktop-file-install --vendor=fedora --delete-original	\
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications		\
  --add-category=X-Fedora --add-category=Network	\
  --remove-category=Utility				\
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# This is a program file and doesn't need to be placed in the library path
rm -f $RPM_BUILD_ROOT/%{python_sitelib}/gnomeblog/%{name}-poster


%clean
rm -rf $RPM_BUILD_ROOT


%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/gnomeblog.schemas >/dev/null || :
fi


%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/gnomeblog.schemas > /dev/null || :


%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/gnomeblog.schemas > /dev/null || :
fi


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_libexecdir}/*
%{_sysconfdir}/gconf/schemas/gnomeblog.schemas
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/applications/*.desktop
%{_libdir}/bonobo/servers/*.server
%dir %{python_sitelib}/gnomeblog
%{python_sitelib}/gnomeblog/*.py
%{python_sitelib}/gnomeblog/*.pyc
%{python_sitelib}/gnomeblog/*.pyo

%changelog
* Wed Oct 31 2007 Heiko Adams <info [at] fedora-blog [dot] de> - 0.9.1-5
- rebuild for rpmforge

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
