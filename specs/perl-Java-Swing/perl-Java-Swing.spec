# $Id$
# Authority: dag
# Upstream: Philip Crow <crow,phil$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Java-Swing

Summary: Perl module providing direct access to the Java Swing API
Name: perl-Java-Swing
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Java-Swing/

Source: http://www.cpan.org/modules/by-module/Java/Java-Swing-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Java-Swing is a Perl module providing direct access to the Java Swing API.

This package contains the following Perl module:

    Java::Swing

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

### Clean up docs
find doc/ example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO doc/ example/
%doc %{_mandir}/man3/Java::Swing.3pm*
%dir %{perl_vendorlib}/Java/
%{perl_vendorlib}/Java/Swing/
%{perl_vendorlib}/Java/Swing.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
