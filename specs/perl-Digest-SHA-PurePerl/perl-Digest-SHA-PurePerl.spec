# $Id$
# Upstream: Mark Shelor <mshelor@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Digest-SHA-PurePerl

Summary: Perl implementation of SHA-1/224/256/384/512
Name: perl-Digest-SHA-PurePerl
Version: 5.48
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-SHA-PurePerl

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSHELOR/Digest-SHA-PurePerl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(FileHandle)
BuildRequires: perl >= 5.003
Requires: perl(FileHandle)
Requires: perl >= 5.003

%filter_from_requires /^perl*/d
%filter_setup


%description

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

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
%doc %{_mandir}/man1/shasum.1*
%doc %{_mandir}/man3/Digest::SHA::PurePerl.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/Digest/SHA/PurePerl.pm
%{_bindir}/shasum

%changelog
* Mon May 31 2010 Christoph Maser <cmr.financial.com> - 5.48-1
- initial package
