# $Id$
# Authority: dag
# Upstream: Joshua Nathaniel Pritikin <jpritikin$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Warp

Summary: Perl module to have control over the flow of time
Name: perl-Time-Warp
Version: 0.5
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Warp/

Source: http://www.cpan.org/modules/by-module/Time/Time-Warp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Time-Warp is a Perl module to have control over the flow of time.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST MANIFEST.SKIP README
%doc %{_mandir}/man3/Time::Warp.3pm*
%dir %{perl_vendorarch}/Time/
%{perl_vendorarch}/Time/Warp.pm
%dir %{perl_vendorarch}/auto/Time/
%{perl_vendorarch}/auto/Time/Warp/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
