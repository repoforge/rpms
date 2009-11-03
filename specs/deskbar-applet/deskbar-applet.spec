# $Id:$
# Authority: hadams

%{!?pyver: %define pyver %(%{__python} -c 'import sys;print(sys.version[0:3])')}
%{!?python_sitelib: %define python_sitelib %(%{__python}%{pyver} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           deskbar-applet
Version:        2.17.2
Release:        3%{?dist}

Summary:        A Gnome applet to allow easy access to various search engines
Group:          Applications/Internet
License:        GPL
URL:            http://live.gnome.org/DeskbarApplet
Source0:        http://ftp.gnome.org/pub/GNOME/sources/deskbar-applet/2.16/%{name}-%{version}.tar.bz2
Source1:        fedorabz.py
Source2:        fedorabz.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gtk2-devel python-devel pygtk2-devel gnome-python2-extras
BuildRequires:  gettext evolution-data-server-devel gnome-desktop-devel
BuildRequires:  libSM-devel gnome-python2-applet desktop-file-utils
BuildRequires:	perl(XML::Parser)
Requires:       gnome-python2 gnome-python2-applet gnome-python2-bonobo
Requires:       gnome-python2-gconf pygtk2 gnome-python2-libwnck
Requires(pre):  GConf2
Requires(post): GConf2 desktop-file-utils
Requires(preun): GConf2 desktop-file-utils
Provides:       deskbar-applet-fedorabz

%description
The goal of DeskbarApplet is to provide an omnipresent versatile search
interface. By typing search terms into the deskbar entry in your panel you are
presented with the search results as you type.

Seaches are handled by a series of plugins. DeskbarApplet provides a simple
interface to manage these plugins to provide you with the search results that
fit your needs.

%prep
%setup -q

%build
%configure --disable-schemas-install
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
hdir="$(grep "^handlersdir=" $RPM_BUILD_ROOT%{_libdir}/pkgconfig/%{name}.pc)"
hdir="${hdir#*=}"
adir="$(grep "^artdir=" $RPM_BUILD_ROOT%{_libdir}/pkgconfig/%{name}.pc)"
adir="${adir#*=}"
install -D -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT$hdir
install -D -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT$adir
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;


%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
    killall -HUP gconfd-2 || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
killall -HUP gconfd-2 || :

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
    killall -HUP gconfd-2 || :
fi

%files -f %{name}.lang
%defattr(-,root,root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_libdir}/%{name}
%{_libdir}/bonobo/servers/Deskbar_Applet.server
%{_libdir}/pkgconfig/%{name}.pc
%{python_sitelib}/deskbar
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Thu Aug 08 2007 Heiko Adams <info@fedora-blog.de> - 2.17.2-3
- rebuild for rpmforge

* Fri Dec 22 2006 Luke Macken <lmacken@redhat.com> - 2.17.2-2
- Add gnome-python2-devel to BuildRequires

* Tue Nov 21 2006 Luke Macken <lmacken@redhat.com> - 2.17.2-1
- 2.17.2

* Wed Nov  2 2006 Luke Macken <lmacken@redhat.com> - 2.16.1-2
- 2.16.1
- Add gnome-python2 to BuildRequires

* Sat Oct 28 2006 Luke Macken <lmacken@redhat.com> - 2.16.0-2
- Rebuild

* Sun Oct  1 2006 Luke Macken <lmacken@redhat.com> - 2.16.0-1
- 2.16.0

* Wed Sep 06 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.15.91-5
- rebuild for FC6
- added BR on XML::Parser

* Sat Aug 19 2006 Luke Macken <lmacken@redhat.com> 2.15.91-3
- Install desktop file correctly

* Wed Aug 17 2006 Luke Macken <lmacken@redhat.com> 2.15.91-1
- 2.15.91
- Require gnome-python2-libwnck

* Mon Aug  7 2006 Luke Macken <lmacken@redhat.com> 2.14.1.1-2
- Rebuild

* Mon Apr 17 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.14.1.1-1
- Upstream update

* Thu Apr 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.14.1-1
- Upstream update
- Decoupled the BZ handler from the upstream tarball

* Tue Mar 14 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.14.0-2
- Fixed bug in Fedora Bugzilla handler (#184231)

* Sun Mar 12 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.14.0-1
- Upstream update

* Fri Feb 24 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.13.91-3
- Added beagle fix (#182728)

* Thu Feb 16 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.13.91-2
- Added patch for prctl thinko
- Added schema scripts

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.13.91-1
- Upstream update

* Thu Feb  2 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.13.90-1
- Upstream update

* Tue Jan  3 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.7-1
- Upstream update

* Mon Dec 12 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.6.1-1
- Upstream update

* Thu Dec  8 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.6-1
- Upstream update

* Thu Dec  1 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.5-2
- Fixed bugs in Fedora BZ handler

* Sun Nov 27 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.5-1
- Upstream update

* Wed Oct  5 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.5.0-1
- Upstream update
- Added Fedora BZ handler

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Mar 19 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.2-3
- %%

* Wed Mar 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.2-2
- Broke %%description at 80 columns

* Tue Mar 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.2-1
- Bump release to 1

* Thu Feb 24 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:0.2-0.iva.0
- Upstream update

* Sun Feb 20 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:0.1-0.iva.0
- Initial RPM release.
