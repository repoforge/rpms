# $Id$
# Authority: dries
# Upstream: David Muir Sharnoff <muir$idiom,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Out

Summary: Buffer output when building CGI programs
Name: perl-CGI-Out
Version: 101.121401
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Out/

Source: http://search.cpan.org/CPAN/authors/id/M/MU/MUIR/modules/CGI-Out-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a helper routine for building CGI programs.  It buffers
stdout until you're completed building your output.  If you should
get an error before you are finished, then it will display a nice
error message (in HTML), log the error, and send email about the
problem.

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
%doc CHANGELOG README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/Out.pm
%{perl_vendorlib}/CGI/BigDeath.pm
%{perl_vendorlib}/CGI/Wrap.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 101.121401-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 101.121401-1
- Initial package.
