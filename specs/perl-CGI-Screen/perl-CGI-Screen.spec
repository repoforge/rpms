# $Id$
# Authority: dries
# Upstream: Ulrich Pfeifer <pfeifer$wait,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Screen

Summary: Extension for easy creation of multi screen CGI scripts
Name: perl-CGI-Screen
Version: 0.119
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Screen/

Source: http://search.cpan.org/CPAN/authors/id/U/UL/ULPFR/CGI-Screen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
CGI::Screen is a subclass of `CGI' which allows the esay(TM) creation of
simple multi screen CGI scripts. By 'multi screen' I mean scripts which
present different screens to the user when called with different
parameters. This is the common case for scripts linking to themselves.
	
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/Screen.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.119-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.119-1
- Initial package.
