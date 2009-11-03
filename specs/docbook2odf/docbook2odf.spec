# $Id$
# Authority: dag
# Upstream: <docbook2odf-devel$lists,sourceforge,net>

Summary: DocBook to OpenDocument XSLT
Name: docbook2odf
Version: 0.256
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://open.comsultia.com/docbook2odf/

Source: http://open.comsultia.com/docbook2odf/dwn/docbook2odf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
Docbook2odf is a toolkit that automaticaly converts DocBook to OASIS
OpenDocument (ODF, the ISO standardized format used for texts,
spreadsheets and presentations). Conversion is based on a XSLT which
makes it easy to convert DocBook->ODF, ODT, ODS and ODP as all these
documents are XML based.

Also goal of docbook2odf is to generate well formatted documents in
OpenDocument, ready to be used in instant, with actually considering
current rules of the Corporate Identity of organizations. Final
results should not be restricted to text like documents but also many
other forms could be generated, like presentations, charts or forms
with images and multimedia.

The result is provided in a one zipped ODF file (.odt/.odp/.ods) with
all required content. There are group of utilities like docbook2odt,
docbook2ods and docbook2odp as docbook2odf is actually universally
converting to these respective formats.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 utils/docbook2odf %{buildroot}%{_bindir}/docbook2odf
%{__install} -Dp -m0644 docs/docbook2odf.1 %{buildroot}%{_mandir}/man1/docbook2odf.1
%{__install} -Dp -m0644 bindings/desktop/docbook2odf.desktop %{buildroot}%{_datadir}/applications/docbook2odf.desktop

%{__install} -d -m0755 %{buildroot}%{_datadir}/docbook2odf/
%{__cp} -av tests/ xsl/ %{buildroot}%{_datadir}/docbook2odf/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license README examples/
%doc %{_mandir}/man1/docbook2odf.1*
%{_bindir}/docbook2odf
%{_datadir}/applications/docbook2odf.desktop
%{_datadir}/docbook2odf/

%changelog
* Sun Dec 21 2008 Dag Wieers <dag@wieers.com> - 0.256-1
- Updated to release 0.256 (svn).

* Wed Jul 25 2007 Dag Wieers <dag@wieers.com> - 0.244-2
- Do not install bindings and libs.

* Mon Jun 18 2007 Dag Wieers <dag@wieers.com> - 0.244-1
- Updated to release 0.244.

* Fri May 18 2007 Dag Wieers <dag@wieers.com> - 0.211-1
- Initial package. (using DAR)
