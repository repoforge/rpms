# $Id$
# Authority: dries
# Upstream: Wim Verhaegen <wimv$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-SimpleVariable

Summary: Simple representation of mathematical variables
Name: perl-Math-SimpleVariable
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-SimpleVariable/

Source: http://search.cpan.org/CPAN/authors/id/W/WI/WIMV/Math-SimpleVariable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Math::SimpleVariable is a simple representation of mathematical
variables, with an obligatory name and an optional value. This class on
itself might not seem very useful at first sight, but you might want to
derive different types of variables for some application. That way,
objects of the derived variable class can be accessed interchangeably
with the here provided protocols.

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
%{perl_vendorlib}/Math/SimpleVariable.pm

%changelog
* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.


