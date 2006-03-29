# $Id$
# Authority: dries
# Upstream: Fabien Tassin <fta+cpan$sofaraway,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-HexDump

Summary: Simple Hexadecial Dumper
Name: perl-Data-HexDump
Version: 0.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-HexDump/

Source: http://search.cpan.org/CPAN/authors/id/F/FT/FTASSIN/Data-HexDump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Dump in hexadecimal the content of a scalar. The result is returned in a
string. Each line of the result consists of the offset in the
source in the leftmost column of each line, followed by one or more
columns of data from the source in hexadecimal. The rightmost column
of each line shows the printable characters (all others are shown
as single dots)

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}
%{__mv} %{buildroot}%{_bindir}/hexdump %{buildroot}%{_bindir}/perlhexdump

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{_bindir}/perlhexdump
%{perl_vendorlib}/Data/HexDump.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
