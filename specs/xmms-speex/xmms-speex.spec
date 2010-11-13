# $Id$
# Authority: matthias

%define xmms_inputdir %(xmms-config --input-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/Input)

Summary: X MultiMedia System input plugin to play speex files
Name: xmms-speex
Version: 0.9.1
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://jzb.rapanden.dk/projects/speex-xmms
Source: http://jzb.rapanden.dk/pub/speex-xmms-%{version}.tar.gz
Patch0: speex-xmms-0.9.1.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7
BuildRequires: xmms-devel, gtk+-devel, speex-devel, libogg-devel


%description
X MultiMedia System input plugin to play speex files.


%prep
%setup -n speex-xmms
%patch0 -p1


%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{xmms_inputdir}/libspeex.so


%changelog
* Mon Jul  5 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-3
- Fix for x86_64.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-2
- Rebuild for Fedora Core 2.

* Mon Jan  5 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-1
- Initial rpm package.

