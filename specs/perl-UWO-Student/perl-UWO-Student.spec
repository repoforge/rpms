# $Id$
# Authority: dag
# Upstream: Jonathan Yu <frequency$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UWO-Student

Summary: Provides Perl object representation of a University of Western Ontario student
Name: perl-UWO-Student
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UWO-Student/

Source: http://www.cpan.org/authors/id/F/FR/FREQUENCY/UWO-Student-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test)
#BuildRequires: perl(Test::More) >= 0.62

%description
Provides Perl object representation of a University of Western Ontario student.

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
%doc MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/UWO::Student.3pm*
%dir %{perl_vendorlib}/UWO/
#%{perl_vendorlib}/UWO/Student/
%{perl_vendorlib}/UWO/Student.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
