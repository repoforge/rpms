# $Id$
# Authority: dries
# Upstream: Alexandre Masselot <alexandre,masselot$genebio,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parallel-Mpich-MPD

Summary: Mpich MPD wrapper
Name: perl-Parallel-Mpich-MPD
Version: 0.9.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parallel-Mpich-MPD/

Source: http://search.cpan.org//CPAN/authors/id/A/AL/ALEXMASS/Parallel-Mpich-MPD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Mpich MPD wrapper.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Parallel::Mpich::MPD*
%{perl_vendorlib}/Parallel/Mpich/MPD.pm
%{perl_vendorlib}/Parallel/Mpich/MPD/
%{_bindir}/mpd-check.pl
%{_bindir}/mpd-kill.pl
%{_bindir}/mpiruns.pl

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Initial package.
