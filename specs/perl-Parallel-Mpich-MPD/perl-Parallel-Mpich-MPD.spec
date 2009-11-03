# $Id$
# Authority: dries
# Upstream: Alexandre Masselot <alexandre,masselot$genebio,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parallel-Mpich-MPD
%define real_version 0.009003

Summary: Mpich MPD wrapper
Name: perl-Parallel-Mpich-MPD
Version: 0.9.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parallel-Mpich-MPD/

Source: http://www.cpan.org/modules/by-module/Parallel/Parallel-Mpich-MPD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(CGI)
BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::All)
BuildRequires: perl(Mail::Sendmail)
BuildRequires: perl(Object::InsideOut)
BuildRequires: perl(Proc::ProcessTable)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Parallel::Mpich::MPD.3pm*
%{_bindir}/mpd-check.pl
%{_bindir}/mpd-kill.pl
%{_bindir}/mpiruns.pl
%dir %{perl_vendorlib}/Parallel/
%dir %{perl_vendorlib}/Parallel/Mpich/
%{perl_vendorlib}/Parallel/Mpich/MPD/
%{perl_vendorlib}/Parallel/Mpich/MPD.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Initial package.
