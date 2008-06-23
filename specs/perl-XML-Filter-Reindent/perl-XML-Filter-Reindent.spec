# $Id$
# Authority: dag
# Upstream: T.J. Mather <tjmather$maxmind,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Filter-Reindent

Summary: Reformats whitespace for pretty printing XML
Name: perl-XML-Filter-Reindent
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Filter-Reindent/

Source: http://www.cpan.org/modules/by-module/XML/XML-Filter-Reindent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Reformats whitespace for pretty printing XML.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/XML::Filter::Reindent.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Filter/
#%{perl_vendorlib}/XML/Filter/Reindent/
%{perl_vendorlib}/XML/Filter/Reindent.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
