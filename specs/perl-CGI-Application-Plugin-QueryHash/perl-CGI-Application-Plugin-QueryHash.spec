# $Id$
# Authority: dries
# Upstream: Graham TerMarsch <cpan$howlingfrog,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Application-Plugin-QueryHash

Summary: Get back query params as hash(ref)
Name: perl-CGI-Application-Plugin-QueryHash
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Application-Plugin-QueryHash/

Source: http://search.cpan.org//CPAN/authors/id/G/GT/GTERMARS/CGI-Application-Plugin-QueryHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Get back query params as hash(ref).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/CGI/Application/Plugin/
%dir %{perl_vendorlib}/CGI/Application/
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Application/Plugin/QueryHash.pm

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
