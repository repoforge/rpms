# $Id$
# Authority: dries
# Upstream: Sam Horrocks <sam$daemoninc,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-SpeedyCGI

Summary: Speed up perl scripts by running them persistently
Name: perl-CGI-SpeedyCGI
Version: 2.22
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-SpeedyCGI/

Source: http://search.cpan.org/CPAN/authors/id/H/HO/HORROCKS/CGI-SpeedyCGI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
SpeedyCGI is a way to run perl scripts persistently, which can make them
run much more quickly. A script can be made to to run persistently by
changing the interpreter line at the top of the script.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
#%doc %{_mandir}/man3/*
%{_bindir}/speedy*
%{perl_vendorlib}/CGI/SpeedyCGI.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.22-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.22-1
- Initial package.
