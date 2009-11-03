# $Id$
# Authority: dag
# Upstream: Jonathan Yu <frequency$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UWO-Directory-Student

Summary: Perform lookups using the University of Western Ontario's student directory
Name: perl-UWO-Directory-Student
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UWO-Directory-Student/

Source: http://www.cpan.org/authors/id/F/FR/FREQUENCY/UWO-Directory-Student-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test)
#BuildRequires: perl(Test::More) >= 0.62

%description
Perform lookups using the University of Western Ontario's student directory.

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
%doc %{_mandir}/man3/UWO::Directory::Student.3pm*
%dir %{perl_vendorlib}/UWO/
%dir %{perl_vendorlib}/UWO/Directory/
#%{perl_vendorlib}/UWO/Directory/Student/
%{perl_vendorlib}/UWO/Directory/Student.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
