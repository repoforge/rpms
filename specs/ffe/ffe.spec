# $Id$
# Authority: dries
# Upstream: <tsja$iki,fi>

Summary: Flat file extractor
Name: ffe
Version: 0.2.4
Release: 1
License: GPL
Group: Applications/Text
URL: http://ff-extractor.sourceforge.net/

Source: http://dl.sf.net/ff-extractor/ffe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ffe is a flat file extractor. It can be used for reading different flat file 
structures and displaying them in different formats. The main areas of use 
are; extracting particular fields or records from a flat file; converting 
data from one format to an other, e.g. from CSV to fixed length; verifying 
a flat file structure; as a testing tool for flat file development; and 
displaying flat file content in human readable form.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__mv} %{buildroot}%{_docdir}/ffe rpmdocs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README rpmdocs/*
%doc %{_mandir}/man1/ffe.1*
%doc %{_infodir}/ffe.info*
%{_bindir}/ffe

%changelog
* Sun Mar 2 2008 Dries Verachtert <dries@ulyssis.org> - 0.2.4-1
- Updated to release 0.2.4.

* Mon Nov  5 2007 Dries Verachtert <dries@ulyssis.org> - 0.2.3-1
- Updated to release 0.2.3.

* Wed May 30 2007 Dries Verachtert <dries@ulyssis.org> - 0.2.2-1
- Updated to release 0.2.2.

* Fri May 11 2007 Dries Verachtert <dries@ulyssis.org> - 0.2.1-1
- Initial package.
