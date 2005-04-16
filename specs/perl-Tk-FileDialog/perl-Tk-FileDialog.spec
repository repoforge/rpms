# $Id$
# Authority: dries
# Upstream: Brent B. Powers <cpan$B2Pi,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk-FileDialog

Summary: Highly configurable File Dialog widget for Perl/Tk
Name: perl-Tk-FileDialog
Version: 1.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk-FileDialog/

Source: http://search.cpan.org/CPAN/authors/id/B/BP/BPOWERS/Tk-FileDialog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Tk::FileDialog is a perl5 package which implements a File Selector
widget.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tk/FileDialog.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
