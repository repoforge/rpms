# $Id$
# Authority: dries
# Upstream: Fabien Tassin <fta+cpan$sofaraway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-HexDump

Summary: Simple Hexadecial Dumper
Name: perl-Data-HexDump
Version: 0.02
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-HexDump/

Source: http://www.cpan.org/modules/by-module/Data/Data-HexDump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;
%{__mv} %{buildroot}%{_bindir}/hexdump %{buildroot}%{_bindir}/perlhexdump

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST MANIFEST.SKIP README
%doc %{_mandir}/man3/Data::HexDump.3pm*
%{_bindir}/perlhexdump
%dir %{perl_vendorlib}/Data/
#%{perl_vendorlib}/Data/HexDump/
%{perl_vendorlib}/Data/HexDump.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
