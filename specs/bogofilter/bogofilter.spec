# Authority: dag

### FIXME: configure has problems finding flex output using soapbox on RHEL3
# Soapbox: 0

%define _requires_exceptions perl

Summary: Fast anti-spam filtering by Bayesian statistical analysis.
Name: bogofilter
Version: 0.16.4
Release: 0
License: GPL
Group: Applications/Internet
URL: http://bogofilter.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/bogofilter/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: flex
Conflicts: bogofilter-static

%description
Bogofilter is a Bayesian spam filter.  In its normal mode of
operation, it takes an email message or other text on standard input,
does a statistical check against lists of "good" and "bad" words, and
returns a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms (including Berkeley DB system),
coded directly in C, and tuned for speed, so it can be used for production
by sites that process a lot of mail.

%prep
%setup

%build
%configure \
  --with-included-gsl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -m0644 %{buildroot}%{_sysconfdir}/bogofilter.cf.example %{buildroot}%{_sysconfdir}/bogofilter.cf

%{__install} -d -m0755 doc-rpm/xml/ doc-rpm/html/
%{__install} -m644 doc/*.xml doc-rpm/xml/
%{__install} -m644 doc/*.html doc-rpm/html/

for dir in contrib; do
	files="$(find "$dir" -maxdepth 1 -type f -print)"
	for file in $files ; do
		case $file in
			*.c|*.o|*.obj|*/Makefile*) continue ;;
			*.1)
				%{__install} -m0644 $file %{buildroot}%{_mandir}/man1/;;
			*)
				%{__install} -d -m0755 %{buildroot}%{_datadir}/bogofilter/$dir/
				%{__install} -m0644 $file %{buildroot}%{_datadir}/bogofilter/$dir/;;
		esac
	done
done

for README in randomtrain; do
  %{__ln_s} -f ../contrib/README.$README doc/README.$README
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES* COPYING METHODS NEWS README* RELEASE.NOTES* TODO
%doc doc/bogofilter-tuning.HOWTO doc/bogofilter-SA-2002-01 doc/integrating* doc/programmer
%doc doc-rpm/html/ doc-rpm/xml/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/bogofilter.cf
%config %{_sysconfdir}/bogofilter.cf.example
%{_bindir}/*
%{_datadir}/bogofilter/

%changelog
* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.16.4-0
- Initial package. (using DAR)
