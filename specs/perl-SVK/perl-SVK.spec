# $Id$
# Authority: dag
# Upstream: Chia-liang Kao (高嘉良) <clkao$clkao,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVK
%define real_version 2.000002

Summary: Perl module that implements a distributed version control system (VCS)
Name: perl-SVK
Version: 2.0.2
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVK/

Source: http://www.cpan.org/authors/id/C/CL/CLKAO/SVK-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(version) >= 0.68
BuildRequires: perl(Algorithm::Annotate)
BuildRequires: perl(Algorithm::Diff) >= 1.19
BuildRequires: perl(YAML::Syck) >= 0.60
BuildRequires: perl(Data::Hierarchy) >= 0.30
BuildRequires: perl(PerlIO::via::dynamic) >= 0.11
BuildRequires: perl(PerlIO::via::symlink) >= 0.02
BuildRequires: perl(IO::Digest)
BuildRequires: perl(SVN::Simple::Edit) >= 0.27
BuildRequires: perl(URI)
BuildRequires: perl(PerlIO::eol) >= 0.13
BuildRequires: perl(Class::Autouse) >= 1.15
BuildRequires: perl(App::CLI)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Path::Class) >= 0.16
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Encode) >= 2.10
BuildRequires: perl(Getopt::Long) >= 2.35
BuildRequires: perl(Pod::Escapes)
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(File::Spec) >= 3.19

%description
perl-SVK is a Perl module that implements a distributed
version control system (VCS).

%prep
%setup -n %{real_name}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find contrib/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ARTISTIC CHANGES CHANGES-1.0 COPYING MANIFEST MANIFEST.SKIP META.yml README SIGNATURE contrib/
%doc %{_mandir}/man3/SVK.3pm*
#%doc %{_mandir}/man3/*.3pm*
#%{perl_vendorlib}/SVK/
%{perl_vendorlib}/SVK.pm

%changelog
* Mon Oct 22 2007 Dries Verachtert <dries@ulyssis.org> - 2.0.2-2
- Fixed the perl(Algorithm::Diff) dependency, thanks to Geoffrey Broadwell.

* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 2.0.2-1
- Initial package. (using DAR)
