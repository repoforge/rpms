# $Id$
# Authority: dries
# Upstream: Jan Pazdziora <adelton$fi,muni,cz>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-STDERR

Summary: Send output of your STDERR to a process or mail
Name: perl-Tie-STDERR
Version: 0.26
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-STDERR/

Source: http://search.cpan.org/CPAN/authors/id/J/JA/JANPAZ/Tie-STDERR-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Send output of your STDERR to a process or mail.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tie/STDERR.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Initial package.
