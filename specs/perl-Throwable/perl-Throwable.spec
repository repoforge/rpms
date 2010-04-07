# $Id$
# Authority: cmr
# Upstream: Ricardo SIGNES <rjbs$cpan,org>
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Throwable

Summary: a role for classes that can be thrown
Name: perl-Throwable
Version: 0.100090
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Throwable/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Throwable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Devel::StackTrace) >= 1.21
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.11
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose) >= 0.87
Requires: perl(Devel::StackTrace) >= 1.21
#Requires: perl(ExtUtils::MakeMaker) >= 6.11
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(Moose) >= 0.87

%filter_from_requires /^perl*/d
%filter_setup


%description
a role for classes that can be thrown.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Throwable.3pm*
%doc %{_mandir}/man3/Throwable::Error.3pm*
%{perl_vendorlib}/Throwable/Error.pm
%{perl_vendorlib}/Throwable.pm

%changelog
* Tue Jan 12 2010 Unknown - 0.100090-1
- Initial package. (using DAR)
