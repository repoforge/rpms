# $Id: xmms-musepack.spec,v 1.1 2004/02/26 17:54:31 thias Exp $

%define xmmsinputdir %(xmms-config --input-plugin-dir)

Summary: X MultiMedia System input plugin to play mpegplus (mpc) files
Name: xmms-musepack
Version: 0.94
Release: 2.fr
License: LGPL
Group: Applications/Multimedia
URL: http://sourceforge.net/projects/mpegplus/
Source: http://dl.sf.net/mpegplus/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7
BuildRequires: xmms-devel, gtk+-devel

%description
X MultiMedia System input plugin to play mpegplus, aka mpc files.

%prep
%setup -q

%build
ARCH="%{optflags}" make %{?_smp_mflags}

%install
rm -rf %{buildroot}
# Patching the Makefile would be overkill for a single file... here we go
# We also change the same to keep more consistent with existing plugins
install -D -m 0755 %{name}-%{version}.so \
    %{buildroot}%{xmmsinputdir}/libmusepack.so

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING.LGPL ChangeLog README_mpc-plugin_english.txt
%lang(fi) %doc README_mpc-plugin_finnish.txt
%lang(de) %doc README_mpc-plugin_german.txt
%lang(ko) %doc README_mpc-plugin_korean.txt
%lang(es) %doc README_mpc-plugin_spanish.txt
%{xmmsinputdir}/libmusepack.so

%changelog
* Fri Feb  6 2004 Matthias Saou <http://freshrpms.net/> 0.94-2.fr
- Override ARCH with %%{optflags} for ppc build.

* Tue Jan 20 2004 Matthias Saou <http://freshrpms.net/> 0.94-1.fr
- Initial rpm package.

