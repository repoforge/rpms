# $Id$
# Authority: matthias

%define xmms_inputdir %(xmms-config --input-plugin-dir)

Summary: X MultiMedia System input plugin to play mpegplus (mpc) files
Name: xmms-musepack
Version: 1.00
Release: 1
License: LGPL
Group: Applications/Multimedia
URL: http://sourceforge.net/projects/mpegplus/
Source: http://dl.sf.net/mpegplus/xmms-musepack-%{version}.tar.gz
Patch: xmms-musepack-1.00-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7
BuildRequires: xmms-devel, gtk+-devel, esound-devel


%description
X MultiMedia System input plugin to play mpegplus, aka mpc files.


%prep
%setup
%patch -p1 -b .makefile


%build
%{__make} %{?_smp_mflags} OPTIONS="%{optflags} -fPIC"


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog README_mpc-plugin_english.txt Wanted
%lang(fi) %doc README_mpc-plugin_finnish.txt
%lang(de) %doc README_mpc-plugin_german.txt
%lang(ko) %doc README_mpc-plugin_korean.txt
%lang(es) %doc README_mpc-plugin_spanish.txt
%{xmms_inputdir}/libmusepack.so


%changelog
* Wed Jul  7 2004 Matthias Saou <http://freshrpms.net/> 1.00-1
- Update to 1.00.
- Added Makefile patch this time, the gcc flags stuff was just too ugly.
- Hmm, now requires esound-devel (esd.h).

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.94-3
- Rebuilt for Fedora Core 2.

* Fri Feb  6 2004 Matthias Saou <http://freshrpms.net/> 0.94-2
- Override ARCH with %%{optflags} for ppc build.

* Tue Jan 20 2004 Matthias Saou <http://freshrpms.net/> 0.94-1
- Initial rpm package.

