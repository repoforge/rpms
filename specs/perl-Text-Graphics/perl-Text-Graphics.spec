# $Id$
# Authority: dries
# Upstream: Stephen Farrell <steve$farrell,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Graphics

Summary: Text graphics rendering toolkit
Name: perl-Text-Graphics
Version: 1.0001
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Graphics/

Source: http://search.cpan.org/CPAN/authors/id/S/SF/SFARRELL/Text-Graphics-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a toolkit for rendering plain text via an API like
that used for graphics rendering in GUI toolkits.  This
package might be used when you want to do sophisticated
rendering of plain text, e.g., for graphing, creating of
complex forms for email and fax, and so on.
	
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
%{perl_vendorlib}/Text/Graphics.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0001-1
- Initial package.
