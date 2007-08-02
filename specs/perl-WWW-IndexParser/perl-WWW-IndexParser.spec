# $Id$
# Authority: dries
# Upstream: James Bromberger <james$rcpt,to>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-IndexParser

Summary: Fetch and parse the directory index from a web server
Name: perl-WWW-IndexParser
Version: 0.8
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-IndexParser/

Source: http://search.cpan.org//CPAN/authors/id/J/JE/JEB/WWW-IndexParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Fetch and parse the directory index from a web server.

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
%doc Changes README
%doc %{_mandir}/man3/WWW::IndexParser*
%{perl_vendorlib}/WWW/IndexParser.pm
%{perl_vendorlib}/WWW/IndexParser/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
