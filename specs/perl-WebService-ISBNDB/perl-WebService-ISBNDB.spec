# $Id$
# Authority: dries
# Upstream: Randy J Ray <rjray$blackperl,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-ISBNDB

Summary: Easy access to isbndb.com
Name: perl-WebService-ISBNDB
Version: 0.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-ISBNDB/

Source: http://search.cpan.org//CPAN/authors/id/R/RJ/RJRAY/WebService-ISBNDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build)

%description
A Perl extension to access isbndb.com.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog.xml README
%doc %{_mandir}/man3/WebService::ISBNDB*
%{perl_vendorlib}/WebService/ISBNDB/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
