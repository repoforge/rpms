# $Id$
# Authority: matthias

%define xmms_inputdir %(xmms-config --input-plugin-dir)

Summary: X MultiMedia System input plugin to play mpegplus (mpc) files
Name: xmms-musepack
Version: 0.94
Release: 3
License: LGPL
Group: Applications/Multimedia
URL: http://sourceforge.net/projects/mpegplus/
Source: http://dl.sf.net/mpegplus/xmms-musepack-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7
BuildRequires: xmms-devel, gtk+-devel


%description
X MultiMedia System input plugin to play mpegplus, aka mpc files.


%prep
%setup


%build
ARCH="%{optflags}" %{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# Patching the Makefile would be overkill for a single file...
# We also change the name to keep more consistent with existing plugins
%{__install} -D -m 0755 %{name}-%{version}.so \
    %{buildroot}%{xmms_inputdir}/libmusepack.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING.LGPL ChangeLog README_mpc-plugin_english.txt
%lang(fi) %doc README_mpc-plugin_finnish.txt
%lang(de) %doc README_mpc-plugin_german.txt
%lang(ko) %doc README_mpc-plugin_korean.txt
%lang(es) %doc README_mpc-plugin_spanish.txt
%{xmms_inputdir}/libmusepack.so


%changelog
* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.94-3
- Rebuilt for Fedora Core 2.

* Fri Feb  6 2004 Matthias Saou <http://freshrpms.net/> 0.94-2
- Override ARCH with %%{optflags} for ppc build.

* Tue Jan 20 2004 Matthias Saou <http://freshrpms.net/> 0.94-1
- Initial rpm package.

