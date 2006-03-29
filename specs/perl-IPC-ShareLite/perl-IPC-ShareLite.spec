# $Id$
# Authority: matthias

%define real_name IPC-ShareLite

Summary: Simple shared memory interface module for perl
Name: perl-IPC-ShareLite
Version: 0.09
Release: 2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-ShareLite/
Source: http://www.cpan.org/modules/by-module/IPC/IPC-ShareLite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: perl >= 0:5.8.0
BuildRequires: perl >= 0:5.8.0

%description
IPC::ShareLite provides a simple interface to shared memory, allowing data to
be efficiently communicated between processes.  Your operating system must
support SysV IPC (shared memory and semaphores) in order to use this module.


%prep
%setup -n %{real_name}-%{version}


%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
    PREFIX="%{buildroot}%{_prefix}" \
    INSTALLDIRS="vendor" << 'EOF'



y




EOF
%{__make} %{?_smp_mflags} \
    OPTIMIZE="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/{.packlist,*.bs}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%{_libdir}/perl5/vendor_perl/*/*
%{_mandir}/man?/*


%changelog
* Wed May 26 2004 Matthias Saou <http://freshrpms.net/> 0.09-2
- Rebuild for Fedora Core 2.

* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net/> 0.09-1
- Initial RPM release.

