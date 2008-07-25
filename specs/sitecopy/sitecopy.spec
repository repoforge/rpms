# $Id$
# Authority: dag
# Upstream Joe Orton <joe$manyfish,co,uk>

### FIXME: xsitecopy support is currently broken
%define _without_xsitecopy 1

Summary: Tool for easily maintaining remote web sites
Name: sitecopy
Version: 0.16.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.manyfish.co.uk/sitecopy/

Source: http://www.manyfish.co.uk/sitecopy/sitecopy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
sitecopy allows you to easily maintain remote Web sites. The program
will upload files to the server which have changed locally, and delete
files from the server which have been removed locally, to keep the
remote site synchronized with the local site, with a single
command. sitecopy will also optionally try to spot files you move
locally, and move them remotely. FTP and WebDAV servers are
supported.

%package -n xsitecopy
Summary: GUI tool for easily maintaining remote web sites
Group: Applications/Internet

%description -n xsitecopy
XSitecopy is a graphical frontend for sitecopy.  Currently it does not
support "resynch" mode, but it does have the advantage of providing
full configuration editing and creation facilities.

%prep
%setup

%build
mkdir sitecopy; cd sitecopy
CFLAGS="%{optflags}" LDFLAGS="-s" ../configure \
    --prefix="%{_prefix}"
%{__make} %{?_smp_mflags}
cd -

%if %{!?_without_xsitecopy:1}0
mkdir xsitecopy; cd xsitecopy
CFLAGS="%{optflags}" LDFLAGS="-s" ../configure \
    --prefix="%{_prefix}" \
    --enable-gnomefe
%{__make} %{?_smp_mflags}
cd -
%endif

%install
%{__rm} -rf %{buildroot}
%{__make} install -C sitecopy \
    DESTDIR="%{buildroot}" \
    mandir="%{_mandir}"
%find_lang %{name}
%if %{!?_without_xsitecopy:1}0
%{__make} install -C xsitecopy \
    DESTDIR="%{buildroot}"
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc BUGS COPYING ChangeLog* INSTALL NEWS README* THANKS TODO
%doc %{_mandir}/man1/sitecopy.1*
%doc %{_mandir}/fr/man1/sitecopy.1*
%{_bindir}/sitecopy
%{_datadir}/sitecopy/
%exclude %{_prefix}/doc/sitecopy/

%if %{!?_without_xsitecopy:1}0
%files -n xsitecopy
%defattr(-, root, root, 0755)
%doc %{_datadir}/gnome/help/xsitecopy/
%{_bindir}/xsitecopy
%{_datadir}/gnome/apps/Internet/*.desktop
%{_datadir}/pixmaps/xsitecopy/
%{_datadir}/xsitecopy/sitecopy-dialogs.glade
%endif

%changelog
* Thu Jul 17 2008 Dag Wieers <dag@wieers.com> - 0.16.5-1
- Updated to release 0.16.5.

* Sun Mar 12 2006 Dag Wieers <dag@wieers.com> - 0.16.3-1
- Updated to release 0.16.3.

* Sun Jan 01 2006 Dag Wieers <dag@wieers.com> - 0.16.2-1
- Updated to release 0.16.2.

* Wed Sep 28 2005 Dag Wieers <dag@wieers.com> - 0.16.1-1
- Updated to release 0.16.1.

* Mon Aug 08 2005 Dag Wieers <dag@wieers.com> - 0.16.0-1
- Updated to release 0.16.0.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 0.15.1-1
- Updated to release 0.15.1.

* Sun Mar 20 2005 Dag Wieers <dag@wieers.com> - 0.15.0-2
- Fixed ownership of the docs. (Oron Peled)

* Mon Mar 07 2005 Dag Wieers <dag@wieers.com> - 0.15.0-1
- Updated to release 0.15.0.

* Thu Feb 17 2005 Dag Wieers <dag@wieers.com> - 0.14.3-1
- Initial package. (using DAR)
