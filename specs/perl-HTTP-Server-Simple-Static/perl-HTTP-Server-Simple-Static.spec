# $Id$
# Authority: dag
# Upstream: Stephen Quinney <sjq-perl$jadevine,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Server-Simple-Static

Summary: Serve static files with HTTP::Server::Simple
Name: perl-HTTP-Server-Simple-Static
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Server-Simple-Static/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Server-Simple-Static-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Serve static files with HTTP::Server::Simple.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTTP::Server::Simple::Static.3pm*
%dir %{perl_vendorlib}/HTTP/
%dir %{perl_vendorlib}/HTTP/Server/
%dir %{perl_vendorlib}/HTTP/Server/Simple/
#%{perl_vendorlib}/HTTP/Server/Simple/Static/
%{perl_vendorlib}/HTTP/Server/Simple/Static.pm
%{perl_vendorlib}/HTTP/Server/Simple/example.pl

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Wed Nov 21 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
