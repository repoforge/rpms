%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define real_name XML-CSV

Name:      perl-XML-CSV
Summary:   XML-CSV - Perl extension converting CSV files to XML
Version:   0.15
Release:   1%{?dist}
Vendor:    CPAN
Packager:  Christoph Maser <cmr@financial.com>
License:   Artistic
Group:     Applications/CPAN
Url:       http://www.cpan.org
Buildarch: noarch
Prefix:    %(echo %{_prefix})
Source:    http://search.cpan.org//CPAN/authors/id/I/IS/ISTERIN/XML-CSV-0.15.tar.gz
BuildRequires: perl >= 0:5.00503
Requires:  perl >= 0:5.00503
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root 


%description
XML::CSV is a new module in is going to be upgraded very often as my time permits.
For the time being it uses CSV_XS module object default values to parse the (*.csv) document and then creates a perl data structure with xml tags names and data. 
At this point it does not allow for a write as you parse interface but is the first upgrade for the next release.  I will also allow more access to the data structures and more documentation.  I will also put in more support for XML, since currently it only allows a simple XML structure.  Currently you can modify the tag structure to allow for attributes.  No DTD support is currently available, but will be implemented in a soon coming release.  As the module will provide both: object and event interfaces, it will be used upon individual needs, system resources, and required performance.  Ofcourse the DOM implementation takes up more resources and in some instances timing, it's the easiest to use.


%prep
%setup -n %{real_name}-%{version}



%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor" %{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/XML
%{perl_vendorlib}/XML/CSV.pm
%dir %{perl_vendorlib}/auto/XML
%dir %{perl_vendorlib}/auto/XML/CSV
%{perl_vendorlib}/auto/XML/CSV/autosplit.ix

%changelog
* Mon Jul 24 2006 cmr@financial.com
- Initial build.
