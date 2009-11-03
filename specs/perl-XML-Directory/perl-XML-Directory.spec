# $Id$
# Authority: dag
# Upstream: Petr Cimprich <petr$gingerall,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Directory

Summary: Perl module that returns a content of directory as XML
Name: perl-XML-Directory
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Directory/

Source: http://www.cpan.org/modules/by-module/XML/XML-Directory-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-XML-Directory is a Perl module that returns a content of directory as XML.

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
find docs/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README docs/ examples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Directory/
%{perl_vendorlib}/XML/Directory.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
