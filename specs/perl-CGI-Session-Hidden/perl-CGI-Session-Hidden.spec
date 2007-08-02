# $Id$
# Authority: dries
# Upstream: Mattia Barbon <mbarbon$users,sourceforge,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Session-Hidden

Summary: Persistent session using hidden fields
Name: perl-CGI-Session-Hidden
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Session-Hidden/

Source: http://search.cpan.org//CPAN/authors/id/M/MB/MBARBON/CGI-Session-Hidden-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build), perl(CGI::Session)

%description
Persistent session using hidden fields.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README.txt
%doc %{_mandir}/man3/CGI::Session::*
%{perl_vendorlib}/CGI/Session/Hidden.pm
%{perl_vendorlib}/CGI/Session/Driver/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
