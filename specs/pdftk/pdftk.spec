# $Id$
# Authority: dag

Summary: PDF Tool Kit
Name: pdftk
Version: 1.12
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://www.accesspdf.com/pdftk/

Source: http://www.pdfhacks.com/pdftk/pdftk-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-java, libgcj-devel

%description
If PDF is electronic paper, then pdftk is an electronic staple-remover,
hole-punch, binder, secret-decoder-ring, and X-Ray-glasses. Pdftk is a simple
tool for doing everyday things with PDF documents. Keep one in the top drawer
of your desktop and use it to:

    * Merge PDF Documents
    * Split PDF Pages into a New Document
    * Decrypt Input as Necessary (Password Required)
    * Encrypt Output as Desired
    * Burst a PDF Document into Single Pages
    * Report on PDF Metrics, including Metadata and Bookmarks
    * Uncompress and Re-Compress Page Streams
    * Repair Corrupted PDF (Where Possible)

%prep
%setup

%build
export -n CLASSPATH
%{__perl} -pi -e 's/-I"\$\(java_libs_root\)"/--classpath="\$(java_libs_root)"/' java_libs/Makefile
%{__make} -C pdftk -f Makefile.RedHat

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 pdftk/pdftk %{buildroot}%{_bindir}/pdftk
%{__install} -Dp -m644 debian/pdftk.1 %{buildroot}%{_mandir}/man1/pdftk.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc pdftk.1.html pdftk.1.txt
%doc %{_mandir}/man1/pdftk.1*
%{_bindir}/pdftk

%changelog
* Tue Oct 03 2006 Dag Wieers <dag@wieers.com> - 1.12-1
- Initial package. (using DAR)
