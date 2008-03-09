# $Id$
# Authority: dag

%define real_name docbook2X

Summary: Convert docbook into man and Texinfo
Name: docbook2x
Version: 0.8.8
Release: 1
License: BSD
Group: Applications/Text
URL: http://docbook2x.sourceforge.net/

Source: http://dl.sf.net/docbook2x/docbook2X-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: %{_bindir}/sgml2xml
BuildRequires: libxslt
BuildRequires: openjade
BuildRequires: perl
BuildRequires: perl(XML::SAX::ParserFactory)
BuildRequires: texinfo
Requires: %{_bindir}/sgml2xml
Requires: libxslt
Requires: openjade
Requires: texinfo

Obsoletes: docbook2X <= %{version}-%{release}
provides: docbook2X = %{version}-%{release}

%description
docbook2x converts DocBook documents into man pages and Texinfo
documents.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --program-transform-name="s/docbook2/db2x_docbook2/"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -c -p"

### Clean up buildroot
%{__mv} -f %{buildroot}%{_docdir}/docbook2X/ rpm-doc/
%{__rm} -f %{buildroot}%{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README THANKS rpm-doc/*
%doc %{_infodir}/docbook2X.info*
%doc %{_infodir}/docbook2man-xslt.info*
%doc %{_infodir}/docbook2texi-xslt.info*
%doc %{_mandir}/man1/db2x_docbook2man.1*
%doc %{_mandir}/man1/db2x_docbook2texi.1*
%doc %{_mandir}/man1/db2x_manxml.1*
%doc %{_mandir}/man1/db2x_texixml.1*
%doc %{_mandir}/man1/db2x_xsltproc.1*
%doc %{_mandir}/man1/sgml2xml-isoent.1*
%doc %{_mandir}/man1/utf8trans.1*
%{_bindir}/db2x_manxml
%{_bindir}/db2x_texixml
%{_bindir}/db2x_xsltproc
%{_bindir}/db2x_docbook2man
%{_bindir}/db2x_docbook2texi
%{_bindir}/sgml2xml-isoent
%{_bindir}/utf8trans
%{_datadir}/docbook2X/

%changelog
* Sun Mar 09 2008 Dag Wieers <dag@wieers.com> - 0.8.8-1
- Initial package. (using DAR)
