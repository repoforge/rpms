# $Id$
# Authority: matthias

%define real_name Error

Summary: Error and exception handling in an OO-ish way module for perl
Name: perl-Error
Version: 0.17008
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Error/
Source: http://www.cpan.org/modules/by-module/Error/Error-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: perl >= 0:5.8.0
BuildRequires: perl >= 0:5.8.0
BuildArch: noarch

%description
The Error package provides two interfaces. Firstly Error provides a procedural
interface to exception handling. Secondly Error is a base class for
errors/exceptions that can either be thrown, for subsequent catch, or can
simply be recorded.


%prep
%setup -n %{real_name}-%{version}


%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
    PREFIX="%{buildroot}%{_prefix}" \
    INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
    OPTIMIZE="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/lib*/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_prefix}/lib*/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%{_prefix}/lib/perl5/vendor_perl/*/*
%{_mandir}/man?/*


%changelog
* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.17008-1
- Updated to release 0.17008.

* Wed May 26 2004 Matthias Saou <http://freshrpms.net/> 0.15-2
- Rebuild for Fedora Core 2.

* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net/> 0.15-1
- Initial RPM release.

