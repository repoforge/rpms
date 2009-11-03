# $Id$
# Authority: dag
# Upstream: Chia-liang Kao (???) <clkao$clkao,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Digest

Summary: Perl module to calculate digests while reading or writing
Name: perl-IO-Digest
Version: 0.10
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Digest/

Source: http://www.cpan.org/modules/by-module/IO/IO-Digest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::via::dynamic)

%description
IO-Digest is a Perl module to calculate digests while reading or writing.

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
%doc CHANGES MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/IO::Digest.3pm*
%dir %{perl_vendorlib}/IO/
%{perl_vendorlib}/IO/Digest.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
