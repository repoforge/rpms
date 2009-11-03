# $Id$
# Authority: dag
# Upstream: Luis Muñoz <luismunoz$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Queue-Dir

Summary: Perl module to manage queue directories where each object is a file
Name: perl-Queue-Dir
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Queue-Dir/

Source: http://www.cpan.org/authors/id/L/LU/LUISMUNOZ/Queue-Dir-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Queue-Dir is a Perl module to manage queue directories
where each object is a file.

This package contains the following Perl module:

    Queue::Dir

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
%doc MANIFEST README
%doc %{_mandir}/man3/Queue::Dir.3pm*
%dir %{perl_vendorlib}/Queue/
%{perl_vendorlib}/Queue/Dir.pm
%{perl_vendorlib}/Queue/flock-test.pl

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
