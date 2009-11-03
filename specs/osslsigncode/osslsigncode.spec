# $Id$
# Authority: matthias

Summary: Tool for Authenticode signing of EXE/CAB files
Name: osslsigncode
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://sourceforge.net/projects/osslsigncode/
Source: http://dl.sf.net/osslsigncode/osslsigncode-%{version}.tar.gz
Patch0: osslsigncode-1.2-hashfix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel, curl-devel

%description
Tool for Authenticode signing of EXE/CAB files.


%prep
%setup
%patch0 -p1 -b .hashfix


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README TODO
%{_bindir}/osslsigncode


%changelog
* Tue Jan 30 2007 Matthias Saou <http://freshrpms.net/> 1.2-1
- Initial RPM release.

