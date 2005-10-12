# $Id$

# Authority: dries
# Upstream: T.J. Mather <tjmather$maxmind,com>

%define real_name XML-XQL
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Query XML tree structures with XQL
Name: perl-XML-XQL
Version: 0.68
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-XQL/

Source: http://www.cpan.org/modules/by-module/XML/XML-XQL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a Perl extension that allows you to perform XQL queries on XML
object trees. Currently only the XML::DOM module is supported, but
other implementations, like XML::Grove, may soon follow.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{_bindir}/xql.pl
%{perl_vendorlib}/XML/XQL.pm
%{perl_vendorlib}/XML/XQL/*

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.68-1
- Initial package.
