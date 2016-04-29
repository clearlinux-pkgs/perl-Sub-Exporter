#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sub-Exporter
Version  : 0.987
Release  : 7
URL      : http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Sub-Exporter-0.987.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Sub-Exporter-0.987.tar.gz
Summary  : 'a sophisticated exporter for custom-built routines'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Sub-Exporter-doc
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Install)

%description
This archive contains the distribution Sub-Exporter,
version 0.987:
a sophisticated exporter for custom-built routines

%package doc
Summary: doc components for the perl-Sub-Exporter package.
Group: Documentation

%description doc
doc components for the perl-Sub-Exporter package.


%prep
%setup -q -n Sub-Exporter-0.987

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Sub/Exporter.pm
/usr/lib/perl5/site_perl/5.22.0/Sub/Exporter/Cookbook.pod
/usr/lib/perl5/site_perl/5.22.0/Sub/Exporter/Tutorial.pod
/usr/lib/perl5/site_perl/5.22.0/Sub/Exporter/Util.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
